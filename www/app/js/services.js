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
var PkiService = angular.module('yapki.services', []);

/**
 * Handle system / error messages through dialogs (native or javascript)
 */
PkiService.factory("SysMsg", ['appdebug', function (appdebug) {
	return {
		showAlert: function (message, title, buttonName) {
			if (appdebug)
				console.log("MCB log ERROR -> " + title + " " + message);
		},
		showAlertAndLog: function (message, objectName, errorMessage) {
			if (appdebug)
				console.log("MCB log ERROR - " + objectName + " -> " + message + " error message: " + errorMessage);
		},
		showInfoAndLog: function (message, objectName, logMessage) {
			if (appdebug)
				console.log("MCB log - " + objectName + " -> " + message + " info message: " + logMessage);
		},
		showConfirmSimple: function (message, title) {
			if (appdebug)
				console.log("MCB log simple confirm -> " + message);
		},
		showConfirm: function (message, confirmCallback, title, buttonLabels) {
			if (appdebug)
				console.log("MCB log simple confirm -> " + message);
		},
		debug: function (message) {
			if (appdebug)
				console.log("MCB log -> " + message);
		},
		device: function () {
			var device = {};
            device.platform = 'Desktop';
            device.model = 'Desktop';
            device.version = '1';
            device.uuid = navigator.userAgent.substr(0, 4);
			return device;
		},
		isOnBrowser: function () {
            return true; // runs on device as device is defined
		},
		isOnAndroid: function () {
			return false; // runs on browser as device is undefined
		},
		isOniOS: function () {
			return false; // runs on browser as device is undefined
		}
	};
}]);


/**
 * Handle system / error messages through dialogs (native or javascript)
 */
PkiService.factory("GlobalYapki", ['SysMsg', 'pkiserver', function (SysMsg, pkiserver) {
    var pkiServerSet = false;
    var pkiServer = pkiserver;
	return {
		isServerSet: function () {
			if (yapkiServerSet)
            {
                return true;
            }
            return false;
		},
		setServer: function (hostname) {
            pkiServer = hostname;
            pkiServerSet = true;
		},
		getServer: function () {
            return(pkiServer);
		}
	};
}]);

