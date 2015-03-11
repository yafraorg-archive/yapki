/** Regular npm dependendencies */
var _ = require('lodash');
var argv = require('minimist')(process.argv.slice(2));
var changelog = require('conventional-changelog');
var fs = require('fs');
var glob = require('glob').sync;
var gulp = require('gulp');
var karma = require('karma').server;
var lazypipe = require('lazypipe');
var mergeStream = require('merge-stream');
var path = require('path');
var pkg = require('./package.json');
var series = require('stream-series');
var through2 = require('through2');

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
    ' * Angular Material Design\n' +
    ' * https://github.com/angular/material\n' +
    ' * @license MIT\n' +
    ' * v' + VERSION + '\n' +
    ' */\n',
  jsBaseFiles: [
    'src/core/**/*.js',
    '!src/core/**/*.spec.js'
  ],
  jsFiles: [
    'src/**/*.js'
  ],
  themeBaseFiles: [
    'src/core/style/variables.scss',
    'src/core/style/mixins.scss'
  ],
  scssBaseFiles: [
    'src/core/style/color-palette.scss',
    'src/core/style/variables.scss',
    'src/core/style/mixins.scss',
    'src/core/style/structure.scss',
    'src/core/style/layout.scss'
  ],
  scssStandaloneFiles: [
    'src/core/style/layout.scss'
  ],
  paths: 'src/{components,services}/**',
  outputDir: 'dist/'
};

var LR_PORT = argv.port || argv.p || 8080;

var buildModes = {
  'closure': {
    transform: utils.addClosurePrefixes,
    outputDir: path.join(config.outputDir, 'modules/closure') + path.sep,
    useBower: false
  },
  'demos': {
    transform: gutil.noop,
    outputDir: path.join(config.outputDir, 'demos') + path.sep,
    useBower: false
  },
  'default': {
    transform: gutil.noop,
    outputDir: path.join(config.outputDir, 'modules/js') + path.sep,
    useBower: true
  }
};

IS_DEMO_BUILD && (BUILD_MODE="demos");
BUILD_MODE = buildModes[BUILD_MODE] || buildModes['default'];


if (IS_RELEASE_BUILD) {
  console.log(
    gutil.colors.red('--release:'),
    'Building release version (minified)...'
  );
}

require('./docs/gulpfile')(gulp, IS_RELEASE_BUILD);



gulp.task('default', ['build']);
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

gulp.task('karma', function(done) {
  var karmaConfig = {
    singleRun: true,
    autoWatch: false,
    browsers : argv.browsers ? argv.browsers.trim().split(',') : ['Chrome'],
    configFile: __dirname + '/config/karma.conf.js'
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
    configFile: __dirname + '/config/karma.conf.js',
    browsers : argv.browsers ? argv.browsers.trim().split(',') : ['Chrome'],
  },done);
});

gulp.task('karma-sauce', function(done) {
  karma.start(require('./config/karma-sauce.conf.js'), done);
});

