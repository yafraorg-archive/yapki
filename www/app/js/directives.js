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
var PkiDirectives = angular.module('yapki.directives', []);

/**
 * Handle external URLs
 */
PkiDirectives.directive("openExternal", ['$window', function ($window) {
	'use strict';

	return {
		restrict: 'E',
		scope: {
			url: "=",
			exit: "&",
			loadStart: "&",
			loadStop: "&",
			loadError: "&"
		},
		transclude: true,
		template: "<a href='' ng-click='openUrl()'><span ng-transclude></span></a>",
		controller: function ($scope) {

			var wrappedFunction = function (action) {
				return function () {
					$scope.$apply(function () {
						action();
					});
				};
			};
			var inAppBrowser;
			$scope.openUrl = function () {
				inAppBrowser = $window.open($scope.url, '_system', 'location=yes');
				//console.log("ext url: opened the url in system browser");
				//if ($scope.exit instanceof Function) {
				//	inAppBrowser.addEventListener('exit', wrappedFunction($scope.closeBrowser));
				//}
			};
			$scope.$on("$destroy", function () {
				if (inAppBrowser !== null) {
					//if ($scope.exit !== undefined) {
					//	inAppBrowser.removeEventListener('exit', wrappedFunction($scope.closeBrowser));
					//}
				}

			});
		}
	};
}]);
