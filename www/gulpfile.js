/** Regular npm dependendencies */
var _ = require('lodash');
var argv = require('minimist')(process.argv.slice(2));
var changelog = require('conventional-changelog');
var fs = require('fs');
var glob = require('glob').sync;
var gulp = require('gulp');
var path = require('path');
var pkg = require('./package.json');
var series = require('stream-series');

/** Gulp dependencies */
var autoprefixer = require('gulp-autoprefixer');
var concat = require('gulp-concat');
var filter = require('gulp-filter');
var gulpif = require('gulp-if');
var gutil = require('gulp-util');
var insert = require('gulp-insert');
var jshint = require('gulp-jshint');
var minifyCss = require('gulp-minify-css');
var ngAnnotate = require('gulp-ng-annotate');
var plumber = require('gulp-plumber');
var rename = require('gulp-rename');
var sass = require('gulp-sass');
var uglify = require('gulp-uglify');
var webserver = require('gulp-webserver');

/** Local dependencies *
var buildConfig = require('./config/build.config');
var utils = require('./scripts/gulp-utils.js');
*/
/** Arguments */
var IS_RELEASE_BUILD = !!argv.release;
var IS_DEMO_BUILD = (!!argv.module || !!argv.m || !!argv.c);
var BUILD_MODE = argv.mode;
var VERSION = argv.version || pkg.version;
var SHA = argv.sha;

/** Grab-bag of build configuration. */
var config = {
  banner:
    '/*!\n' +
    ' * Yafra - YAPKI tool\n' +
    ' * https://github.com/yafraorg/yafra\n' +
    ' * @license Apache\n' +
    ' * v' + VERSION + '\n' +
    ' */\n',
  jsBaseFiles: [
    'app/js/**/*.js',
    '!app/js/**/*.spec.js'
  ],
  jsFiles: [
    'app/js/**/*.js'
  ],
  themeBaseFiles: [
    'app/assets/app.scss'
  ],
  scssBaseFiles: [
    'app/assets/color-palette.scss'
  ],
  scssStandaloneFiles: [
    'app/assets/layout.scss'
  ],
  paths: 'app/{components,services}/**',
  outputDir: 'dist/'
};

var LR_PORT = argv.port || argv.p || 8080;

//require('../docs/gulpfile')(gulp, IS_RELEASE_BUILD);



gulp.task('default', ['validate', 'changelog']);
gulp.task('validate', ['jshint', 'karma']);
gulp.task('changelog', function(done) {
  var options = {
    repository: 'https://github.com/yafraorg/yapki',
    version: VERSION,
    file: 'CHANGELOG.md'
  };
  if (SHA) {
    options.from = SHA;
  }
  changelog(options, function(err, log) {
    fs.writeFileSync(__dirname + '/CHANGELOG.md', log);
  });
});
gulp.task('jshint', function() {
  return gulp.src(
    config.jsFiles
  )
    .pipe(jshint('.jshintrc'))
    .pipe(jshint.reporter(require('jshint-summary')({
      fileColCol: ',bold',
      positionCol: ',bold',
      codeCol: 'green,bold',
      reasonCol: 'cyan'
    })))
    .pipe(jshint.reporter('fail'));
});


/** *****************************************
 *
 * Tasks for Karma Test
 *
 ** ***************************************** */

var karma = require('karma').server;

gulp.task('karma', function(done) {
  var karmaConfig = {
    singleRun: true,
    autoWatch: false,
    //browsers : argv.browsers ? argv.browsers.trim().split(',') : ['Chrome'],
    configFile: __dirname + '/karma.conf.js'
  };

  gutil.log('Running unit tests on unminified source.');
  karma.start(karmaConfig, done);

  //function testMinified() {
  //  gutil.log('Running unit tests on minified source.');
  //  buildJs(true);
  //  karmaConfig.releaseMode = true;
  //  karma.start(karmaConfig, done);
  //}
});

gulp.task('karma-watch', function(done) {
  karma.start({
    singleRun:false,
    autoWatch:true,
    configFile: __dirname + '/karma.conf.js',
    //browsers : argv.browsers ? argv.browsers.trim().split(',') : ['Chrome']
  },done);
});

var protractor = require("gulp-protractor").protractor;

// Start a standalone server
var webdriver_standalone = require('gulp-protractor').webdriver_standalone;

// Download and update the selenium driver
var webdriver_update = require('gulp-protractor').webdriver_update;

// Downloads the selenium webdriver
gulp.task('webdriver_update', webdriver_update);

// Start the standalone selenium server
// NOTE: This is not needed if you reference the
// seleniumServerJar in your protractor.conf.js
gulp.task('webdriver_standalone', webdriver_standalone);


// Setting up the test task
gulp.task('protractor', ['webdriver_update'], function(cb) {
gulp.src(["./e2e-tests/scenarios.js"])
    .pipe(protractor({
        configFile: "e2e-tests/protractor.conf.js"}))
    .on('error', function(e) { console.log(e)
    }).on('end', cb);
});
