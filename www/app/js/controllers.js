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

'use strict';
var PkiController = angular.module('yapki.controllers', []);


/**
 * Default controller
 */
PkiController.controller('DefaultCtrl', ['$scope', '$mdSidenav', 'SysMsg', function ($scope, $mdSidenav, SysMsg) {
  SysMsg.debug("start DefaultCtrl");
  $scope.toggleLeft = function() {
    $mdSidenav('left').toggle()
                      .then(function(){
                          SysMsg.debug("toggle left is done");
                      });
  };
  $scope.close = function() {
    $mdSidenav('left').close()
                      .then(function(){
                        SysMsg.debug("close LEFT is done");
                      });
  };

}]);

/**
 * Certificate Database controller
 */
PkiController.controller('DbCtrl', ['$scope', 'SysMsg', 'Database', function ($scope, SysMsg, Database) {
    SysMsg.debug("start DbCtrl");

	// get server info
	Database.query(
		function (response) {
			$scope.data.db = response;
		},
		function (error) {
			SysMsg.showAlertAndLog('no network access to server', 'DbCtrl', JSON.stringify(error));
		}
	);

}]);

/**
 * Certificate Request controller
 */
PkiController.controller('ReqCtrl', ['$scope', '$mdSidenav', 'SysMsg', function ($scope, $mdSidenav, SysMsg) {
}]);

/**
 * Login controller
 */
PkiController.controller('LoginCtrl', ['$scope', 'GlobalYapki', 'SysMsg', function ($scope, GlobalYapki, SysMsg) {
    SysMsg.debug("start LoginCtrl");
    $scope.hostname = GlobalYapki.getServer();
    SysMsg.debug("start hostname is: ", $scope.hostname);

	$scope.setHost = function () {
		SysMsg.debug('Set pki server hostname to: ', $scope.hostname);
        GlobalYapki.setServer($scope.hostname);
        SysMsg.debug("new hostname set");
	};

}]);

/**
 * HELP controller.
 */
PkiController.controller('HelpCtrl', ['$scope', 'appversion', 'SysMsg', 'pkihelp', 'ServerInfo', function ($scope, appversion, SysMsg, pkihelp, ServerInfo) {
	// Help controller, giving some about infos
	$scope.version = appversion;
	$scope.device = SysMsg.device();
	$scope.url = pkihelp;
	$scope.data = {};

	SysMsg.debug("help web page is: " + $scope.url);

	$scope.closeBrowser = function () {
		SysMsg.debug('Closed browser');
	};

	// get server info
	ServerInfo.get(
		function (response) {
			$scope.data.serverinfo = response;
		},
		function (error) {
			SysMsg.showAlertAndLog('no network access to server', 'HelpCtrl', JSON.stringify(error));
		}
	);


}]);
