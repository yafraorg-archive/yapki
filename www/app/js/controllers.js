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
var PkiController = angular.module('yapki.controllers', []);


/**
 * Default controller
 */
PkiController.controller('DefaultCtrl', ['$scope', '$mdSidenav', 'SysMsg', function ($scope, $mdSidenav, SysMsg) {
	'use strict';
  $scope.openLeftMenu = function() {
    $mdSidenav('left').toggle();
  };

}]);


/**
 * A simple example service that returns some data.
 */
PkiController.controller('HelpCtrl', ['$scope', 'appversion', 'SysMsg', 'yapkihelp', function ($scope, appversion, SysMsg, yapkihelp) {
	// Help controller, giving some about infos
	'use strict';
	$scope.version = appversion;
	$scope.device = SysMsg.device();
	$scope.url = yapkihelp;
	SysMsg.debug("help web page is: " + $scope.url);
	$scope.closeBrowser = function () {
		$scope.infotext = 'Closed browser';
	};
	$scope.loadStart = function () {
		$scope.infotext = 'load start browser';
	};
	$scope.loadStop = function () {
		$scope.infotext = 'load stop browser';
	};
	$scope.loadError = function () {
		$scope.infotext = 'load error with browser';
	};
}]);
