module.exports = function(config){
  config.set({

    basePath : './',

    files : [
        'app/bower_components/angular/angular.js',
        'app/bower_components/angular-ui-router/release/angular-ui-router.js',
        'app/bower_components/angular-resource/angular-resource.js',
        'app/bower_components/angular-aria/angular-aria.js',
        'app/bower_components/angular-animate/angular-animate.js',
        'app/bower_components/angular-mocks/angular-mocks.js',
        'app/bower_components/angular-material/angular-material.js',
        'app/js/*.js',
        'tests/*Test.js'
    ],

    autoWatch : true,

    frameworks: ['jasmine'],

    browsers : ['Chrome'],

    plugins : [
            'karma-chrome-launcher',
            'karma-coverage',
            'karma-firefox-launcher',
            'karma-jasmine',
            'karma-junit-reporter'
            ],

    junitReporter : {
      outputFile: '../shippable/testresults/karmatests.xml',
      suite: 'unit'
    },

    singleRun: true,
    reporters: ['progress', 'coverage', 'junit'],
    preprocessors: { '*.js': ['coverage'] }
  });
};
