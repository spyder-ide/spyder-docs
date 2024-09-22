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
    rules: {
      "no-var": "off",
    },
  },
];
