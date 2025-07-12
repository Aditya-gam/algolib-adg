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

    // Relax body line length to allow longer descriptions
    'body-max-line-length': [2, 'always', 300],

    // Relax footer line length to allow longer descriptions
    'footer-max-line-length': [2, 'always', 300],

    // Require subject to not be empty
    'subject-empty': [2, 'never'],

    // Require type to not be empty
    'type-empty': [2, 'never'],

    // Make scope validation more flexible - allow any valid scope
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

        // Additional scopes used in commits
        'scaffolding',
        'property',
        'runtime',
        'quality-gate',
      ],
    ],

    // Enforce footer format
    'footer-leading-blank': [2, 'always'],

    // Enforce body format
    'body-leading-blank': [2, 'always'],

    // Enforce body max length - reduced to 800 characters to be more reasonable
    'body-max-length': [2, 'always', 800],
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
