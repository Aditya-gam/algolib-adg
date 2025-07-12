export default {
  extends: ['@commitlint/config-conventional'],
  rules: {
    // Enforce conventional commit format
    'type-enum': [
      2,
      'always',
      [
        'feat',     // New features
        'fix',      // Bug fixes
        'docs',     // Documentation changes
        'style',    // Code style changes (formatting, etc.)
        'refactor', // Code refactoring
        'test',     // Adding or updating tests
        'chore',    // Maintenance tasks
        'perf',     // Performance improvements
        'ci',       // CI/CD changes
        'build',    // Build system changes
        'revert',   // Revert previous commits
      ],
    ],

    // Enforce lowercase types
    'type-case': [2, 'always', 'lower-case'],

    // Enforce lowercase scopes
    'scope-case': [2, 'always', 'lower-case'],

    // Enforce lowercase subjects
    'subject-case': [2, 'always', 'lower-case'],

    // Require subject to end without period
    'subject-full-stop': [2, 'never', '.'],

    // Enforce subject line length
    'subject-max-length': [2, 'always', 72],

    // Enforce header line length
    'header-max-length': [2, 'always', 100],

    // Enforce body line length
    'body-max-line-length': [2, 'always', 100],

    // Enforce footer line length
    'footer-max-line-length': [2, 'always', 100],

    // Require subject to not be empty
    'subject-empty': [2, 'never'],

    // Require type to not be empty
    'type-empty': [2, 'never'],

    // Enforce scope format (optional but must be valid if present)
    'scope-enum': [
      2,
      'always',
      [
        // Algorithm scopes
        'algorithms',
        'searching',
        'sorting',
        'graph',
        'dynamic-programming',
        'greedy',
        'backtracking',
        'math',

        // Data structure scopes
        'data-structures',
        'tree',
        'heap',
        'graph-ds',
        'linked-list',
        'stack',
        'queue',
        'trie',

        // Infrastructure scopes
        'ci',
        'cd',
        'docs',
        'tests',
        'benchmarks',
        'api',
        'db',
        'security',
        'performance',

        // General scopes
        'core',
        'utils',
        'interfaces',
        'typing',
        'deps',
        'config',
        'scripts',
        'tools',
      ],
    ],

    // Enforce breaking change format
    'breaking-change': [2, 'always'],

    // Enforce footer format
    'footer-leading-blank': [2, 'always'],

    // Enforce body format
    'body-leading-blank': [2, 'always'],

    // Enforce body max length
    'body-max-length': [2, 'always', 1000],
  },

  // Custom parser for better error messages
  parserPreset: {
    parserOpts: {
      issuePrefixes: ['#'],
      referenceActions: ['closes', 'fixes', 'resolves', 'reverts'],
    },
  },

  // Helpful error messages
  helpUrl: 'https://github.com/conventional-changelog/commitlint/#what-is-commitlint',
};
