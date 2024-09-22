// Configuration file for eslint

const neostandard = require("neostandard");

module.exports = [
  ...neostandard({noStyle: true}),
  {
    languageOptions: {
      sourceType: "script",
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
