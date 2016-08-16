'use strict';

angular
  .module('autopy')
  .config(
    ['$locationProvider', '$routeProvider',
    function config($locationProvider, $routeProvider) {
      $locationProvider.hashPrefix('!');

      $routeProvider.
        when('/vehicle-types', {
          template: '<vehicle-types-list></vehicle-types-list>'
        }).
        otherwise('/vehicle-types');
    }
  ]);
