var ScreenShotReporter = require('protractor-screenshot-reporter');

exports.config = {
  allScriptsTimeout: 11000,

  specs: [
    '*.js'
  ],

  capabilities: {
    'browserName': 'chrome'
  },

  baseUrl: 'http://localhost:8081/',

  framework: 'jasmine',

  jasmineNodeOpts: {
    defaultTimeoutInterval: 30000
  },

  onPrepare: function() {
      // Add a screenshot reporter and store screenshots to `/tmp/screnshots`:
      jasmine.getEnv().addReporter(new ScreenShotReporter({
         baseDirectory: '/tmp/screenshots'
      }));
   }
};
