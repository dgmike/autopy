'use strict';

angular
  .module('manufacturers')
  .component('manufacturersSearch', {
    templateUrl: 'static/app/manufacturers/manufacturers-search.template.html',
    controller: function manufacturersSearchController($location, $http, $scope) {
      var self = this;

      self.id__exact = $location.search().id__exact;
      self.name__icontains = $location.search().name__icontains;
      self.search = $location.search().search;
      self.vehicle_type__id__exact = $location.search().vehicle_type__id__exact;
      $scope.vehicle_types = [];

      $http.get('/api/vehicle-types')
        .then(
          function responseSuccess(response) {
            $scope.vehicle_types = response.data._embedded.vehicle_types;

            angular.forEach(response.data._embedded.vehicle_types, function (item) {
              if ($location.search().vehicle_type__id__exact == item.id) {
                self.vehicle_type__id__exact = item;
              }
            });
          },
          function responseError(response) {}
         );

      self.doSearch = function (elmId, extraFields) {
        var extraFields = extraFields || {};
        var params = {};
        var serializatedArray = angular.element(elmId).serializeArray();
        $(serializatedArray)
          .each(function(_k, v) {
            if (self[v.name] && self[v.name].id) {
              return params[v.name] = self[v.name].id;
            }
            return params[v.name] = self[v.name];
          });
        params = angular.merge({}, params, extraFields);
        $location.search(params);
      };

      self.basicSearch = function () {
        self.doSearch('#basicSearchForm');
      };

      self.advancedSearch = function () {
        self.doSearch('#advancedSearchForm', {search: 'advanced'});
      };
    }
  });
