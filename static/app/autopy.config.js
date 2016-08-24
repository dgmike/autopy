'use strict';

angular
  .module('autopy')
  .config(
    ['$locationProvider', '$routeProvider', '$httpProvider',
    function config($locationProvider, $routeProvider, $httpProvider) {
      $httpProvider.defaults.xsrfCookieName = 'csrftoken';
      $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';

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
        .when('/manufacturers', {
          template: '<manufacturers-list></manufacturers-list>'
        })
        .when('/manufacturers/new', {
          template: '<manufacturers-new></manufacturers-new>'
        })
        .when('/manufacturers/:id/edit', {
          template: '<manufacturers-edit></manufacturers-edit>'
        })
        .when('/manufacturers/:id', {
          template: '<manufacturers-show></manufacturers-show>'
        })
        .when('/vehicles', {
          template: '<vehicles-list></vehicles-list>'
        })
        .when('/vehicles/new', {
          template: '<vehicles-new></vehicles-new>'
        })
        .when('/vehicles/:id/edit', {
          template: '<vehicles-edit></vehicles-edit>'
        })
        .when('/vehicles/:id', {
          template: '<vehicles-show></vehicles-show>'
        })
        .otherwise('/vehicle-types');
    }
  ]);
