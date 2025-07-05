from pathlib import Path
from typing import List

import yaml
from pydantic import BaseModel, RootModel


class Complexity(BaseModel):
    time_worst: str
    time_average: str
    time_best: str
    space_worst: str


class Parameter(BaseModel):
    name: str
    type: str
    description: str


class Returns(BaseModel):
    type: str
    description: str


class AlgorithmSpec(BaseModel):
    name: str
    description: str
    category: str
    complexity: Complexity
    parameters: List[Parameter]
    returns: Returns
    dependencies: List[str]

    @classmethod
    def from_file(cls, path: Path) -> "AlgorithmSpec":
        with open(path, "r") as f:
            data = yaml.safe_load(f)
        return cls(**data)


class SpecList(RootModel[List[AlgorithmSpec]]):
    root: List[AlgorithmSpec]
