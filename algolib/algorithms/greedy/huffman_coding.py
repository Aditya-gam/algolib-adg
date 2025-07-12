"""Huffman Coding greedy algorithm implementation."""

import heapq
from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple


class HuffmanNode:
    """Node in a Huffman tree."""

    def __init__(
        self,
        char: Optional[str],
        freq: int,
        left: Optional["HuffmanNode"] = None,
        right: Optional["HuffmanNode"] = None,
    ) -> None:
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right

    def __lt__(self, other: "HuffmanNode") -> bool:  # pragma: no cover
        return self.freq < other.freq

    def __repr__(self) -> str:  # pragma: no cover
        return f"HuffmanNode(char={self.char}, freq={self.freq})"


@dataclass(slots=True, init=False)
class HuffmanCoding:
    """Greedy Huffman coding compressor/decompressor."""

    def build_tree(self, text: str, freq_map: Dict[str, int]) -> Optional[HuffmanNode]:
        if not text:
            raise ValueError("Text cannot be empty")

        # Handle single-character text
        if len(freq_map) == 1:
            ch = next(iter(freq_map))
            return HuffmanNode(ch, freq_map[ch])

        heap: List[HuffmanNode] = [HuffmanNode(ch, fr) for ch, fr in freq_map.items()]
        heapq.heapify(heap)

        while len(heap) > 1:
            left = heapq.heappop(heap)
            right = heapq.heappop(heap)
            merged = HuffmanNode(None, left.freq + right.freq, left, right)
            heapq.heappush(heap, merged)

        return heap[0]

    def _generate_codes_recursive(
        self, node: Optional[HuffmanNode], code: str, codes: Dict[str, str]
    ) -> None:
        if node is None:
            return
        if node.char is not None:
            codes[node.char] = code or "0"
            return
        self._generate_codes_recursive(node.left, code + "0", codes)
        self._generate_codes_recursive(node.right, code + "1", codes)

    def generate_codes(self, root: Optional[HuffmanNode]) -> Dict[str, str]:
        if root is None:
            return {}
        codes: Dict[str, str] = {}
        if root.char is not None:
            codes[root.char] = "0"
            return codes
        self._generate_codes_recursive(root, "", codes)
        return codes

    def encode(self, text: str, codes: Dict[str, str]) -> str:
        encoded: List[str] = []
        for ch in text:
            if ch not in codes:
                raise ValueError(f"Character '{ch}' not found in codes")
            encoded.append(codes[ch])
        return "".join(encoded)

    def _traverse_huffman_tree(self, bit: str, current: HuffmanNode) -> HuffmanNode:
        if bit not in "01":
            raise ValueError(f"Invalid bit '{bit}' in encoded string")

        next_node = current.left if bit == "0" else current.right
        if next_node is None:
            raise ValueError("Invalid encoded string: path leads to None")
        return next_node

    def decode(self, encoded: str, root: Optional[HuffmanNode], freq_map: Dict[str, int]) -> str:
        if root is None:
            raise ValueError("Cannot decode with None tree")
        if not encoded:
            return ""
        if root.char is not None:
            # If the tree is just a single node, the decoded string is that character repeated
            return root.char * len(encoded)

        decoded: List[str] = []
        current = root
        for bit in encoded:
            current = self._traverse_huffman_tree(bit, current)
            if current.char is not None:
                decoded.append(current.char)
                current = root

        # Final check for incomplete sequences
        if current != root and not (len(freq_map) == 1 and root.char is not None):
            raise ValueError("Incomplete encoded string")

        return "".join(decoded)

    def compress(self, text: str) -> Tuple[str, Dict[str, str], Optional[HuffmanNode]]:
        freq_map: Dict[str, int] = {}
        for ch in text:
            freq_map[ch] = freq_map.get(ch, 0) + 1

        tree = self.build_tree(text, freq_map)
        codes = self.generate_codes(tree)
        encoded = self.encode(text, codes)
        return encoded, codes, tree

    def calculate_compression_ratio(self, original: str, encoded: str) -> float:
        if not original:
            return 0.0
        original_bits = len(original) * 8  # ASCII assumption
        encoded_bits = len(encoded)
        return encoded_bits / original_bits if original_bits > 0 else 0.0
