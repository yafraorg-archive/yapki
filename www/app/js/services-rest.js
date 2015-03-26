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
var PkiRestServices = angular.module('yapki.services-rest', []);

/* ----------------------------------- Login / Userdevice services ------------------------*/
/**
 * Login / Registration
 * send unprotected registration of oauth apikey and email using the registered email
 */
PkiRestServices.factory('ServerInfo', ['$resource', 'GlobalYapki', function ($resource, GlobalYapki) {
	return $resource((GlobalYapki.getServer() + '/info'), null, {
		get: {
			method: 'GET',
			isArray: false,
			headers: {'Accept': 'application/json', 'Content-Type': 'application/json'}
		}
	});
}]);


/**
 * Query Program/Events per section
 * Query an event detail
 */
PkiRestServices.factory('Database', ['$resource', 'GlobalYapki', function ($resource, GlobalYapki) {
	return $resource((GlobalYapki.getServer() + '/db/'), null, {
		query: {
			method: 'GET',
			isArray: true,
			headers: {'Accept': 'application/json', 'Content-Type': 'application/json'}
		}
	});
}]);
