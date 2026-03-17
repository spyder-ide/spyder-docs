// Configuration file for eslint

const neostandard = require("neostandard");

module.exports = [
  ...neostandard({noStyle: true}),
  {
    languageOptions: {
      sourceType: "script",
      parserOptions: {
        ecmaFeatures: {
          impliedStrict: true,
        },
      },
      globals: {
        browser: true,
        jquery: true,
      },
    },
    linterOptions: {
      reportUnusedDisableDirectives: "warn",
    },
  },
];
