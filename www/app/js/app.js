/*
 * Licensed to the Apache Software Foundation (ASF) under one
 * or more contributor license agreements.  See the NOTICE file
 * distributed with this work for additional information
 * regarding copyright ownership.  The ASF licenses this file
 * to you under the Apache License, Version 2.0 (the
 * "License"); you may not use this file except in compliance
 * with the License.  You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing,
 * software distributed under the License is distributed on an
 * "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 * KIND, either express or implied.  See the License for the
 * specific language governing permissions and limitations
 * under the License.
 */

// angular.module is a global place for creating, registering and retrieving Angular modules
// 'starter' is the name of this angular module example (also set in a <body> attribute in index.html)
// the 2nd parameter is an array or 'requires'
// 'starter.services' is found in services.js
// 'starter.controllers' is found in controllers.js
// Declare app level module which depends on filters, and services
var PkiApp = angular.module('yapkiApp', [
    'ui.router',
    'ngResource',
    'ngMaterial',
    'yapki.services',
    'yapki.services-rest',
    'yapki.controllers']);


// Version
PkiApp.constant('appversion', '1.0.1');

// Debug mode
PkiApp.constant('appdebug', true);

// Server URL
//PkiApp.constant('pkiserver', 'http://pki.yafra.org:8080');
PkiApp.constant('pkiserver', 'http://localhost:8080');
//PkiApp.constant('pkiserver', 'http://192.168.9.10:8080');

PkiApp.constant('pkihelp', 'http://pki.yafra.org/');


PkiApp.run(['SysMsg', function (SysMsg) {
    'use strict';
    SysMsg.debug("run() - runs on Browser");
}]);

/**
 * Routing table including associated controllers.
 */
PkiApp.config(['$stateProvider', '$urlRouterProvider', function ($stateProvider, $urlRouterProvider) {
    'use strict';

    $stateProvider
        .state('menu', {url: "/pki", abstract: true, templateUrl: "templates/main.html", controller: 'DefaultCtrl'})
        .state('menu.req', {
            url: '/req',
            views: {'menuContent': {templateUrl: 'templates/reqView.html', controller: 'ReqCtrl'}}
        })
        .state('menu.db', {
            url: '/db',
            views: {'menuContent': {templateUrl: 'templates/dbView.html', controller: 'DbCtrl'}}
        })
        .state('menu.help', {
            url: '/help',
            views: {'menuContent': {templateUrl: 'templates/helpView.html', controller: 'HelpCtrl'}}
        });

    // if none of the above states are matched, use this as the fallback
    $urlRouterProvider.otherwise('/pki/db');
}]);
