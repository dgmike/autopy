'use strict';

angular
  .module('autopy')
  .config(
    ['$locationProvider', '$routeProvider',
    function config($locationProvider, $routeProvider) {
      $locationProvider.hashPrefix('!');

      $routeProvider
        .when('/vehicle-types', {
          template: '<vehicle-types-list></vehicle-types-list>'
        })
        .when('/vehicle-types/new', {
          template: '<vehicle-types-new></vehicle-types-new>'
        })
        .when('/vehicle-types/:id/edit', {
          template: '<vehicle-types-edit></vehicle-types-edit>'
        })
        .when('/vehicle-types/:id', {
          template: '<vehicle-types-show></vehicle-types-show>'
        })
        .otherwise('/vehicle-types');
    }
  ]);
