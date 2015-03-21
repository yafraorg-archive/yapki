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
var PkiFilters = angular.module('yapki.filters', []);

/**
 * @ngdoc filter
 * @name parseUrl
 * @kind function
 *
 * @description
 * Finds links in text input and turns them into html links. Supports http/https/ftp/mailto and
 * plain email address links.
 *
 * Requires the {@link ngSanitize `ngSanitize`} module to be installed.
 *
 * @param {string} text Input text.
 * @param {string} target Window (_blank|_self|_parent|_top) or named frame to open links in.
 * @returns {string} Html-linkified text.
 *
 * @usage
 <span ng-bind-html="text_expression | parseUrl | trustHtml"></span>
 *
 * @example
 <example module="linkyExample" deps="angular-sanitize.js">
 <file name="index.html">
 <div ng-bind-html="snippet | parseUrl | trustHtml"></div>
 </example>
 */
PkiFilters.filter('parseUrl', function() {
	var urls = /(\b(https?|ftp):\/\/[A-Z0-9+&@#\/%?=~_|!:,.;-]*[-A-Z0-9+&@#\/%=~_|])/gim;
	var emails = /(\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,6})/gim;

	return function (text) {
		if (text.match(urls)) {
			text = text.replace(urls, "<a onclick=\"angular.element(this).scope().exLink(this);return false;\" href=\"$1\">$1</a>");
		}
		if (text.match(emails)) {
			text = text.replace(emails, "<a href=\"mailto:$1\">$1</a>");
		}

		return text;
	};
});


/**
 * @ngdoc filter
 * @name trustHtml
 * @kind function
 *
 * @description
 * mark input as html ready text.
 *
 * Requires the {@link ngSanitize `ngSanitize`} module to be installed.
 *
 * @param {string} text Input text.
 * @returns {string} Html.
 *
 * @usage
 <span ng-bind-html="text_expression | parseUrl | trustHtml"></span>
 *
 * @example
 <example module="linkyExample" deps="angular-sanitize.js">
 <file name="index.html">
 <div ng-bind-html="snippet | parseUrl | trustHtml"></div>
 </example>
 */
PkiFilters.filter('trustHtml', ['$sce', function($sce){
	return function(text) {
		return $sce.trustAsHtml(text);
	};
}]);

// formats a number as a latitude (e.g. 40.46... => "40°27'44"N")
PkiFilters.filter('lat', function () {
	return function (input, decimals) {
		if (!decimals) {decimals = 0;}
		input = input * 1;
		var ns = input > 0 ? "N" : "S";
		input = Math.abs(input);
		var deg = Math.floor(input);
		var min = Math.floor((input - deg) * 60);
		var sec = ((input - deg - min / 60) * 3600).toFixed(decimals);
		return deg + "°" + min + "'" + sec + '"' + ns;
	};
});

// formats a number as a longitude (e.g. -80.02... => "80°1'24"W")
PkiFilters.filter('lon', function () {
	return function (input, decimals) {
		if (!decimals) {decimals = 0;}
		input = input * 1;
		var ew = input > 0 ? "E" : "W";
		input = Math.abs(input);
		var deg = Math.floor(input);
		var min = Math.floor((input - deg) * 60);
		var sec = ((input - deg - min / 60) * 3600).toFixed(decimals);
		return deg + "°" + min + "'" + sec + '"' + ew;
	};
});
