'use strict';

angular
  .module('manufacturers')
  .component('manufacturersSearch', {
    templateUrl: 'static/app/manufacturers/manufacturers-search.template.html',
    controller: function manufacturersSearchController($location, $rootScope) {
      var self = this;
      self.id__exact = $location.search().id__exact;
      self.name__icontains = $location.search().name__icontains;
      self.search = $location.search().search;

      self.doSearch = function (elmId, extraFields) {
        var extraFields = extraFields || {};
        var params = {};
        var serializatedArray = angular.element(elmId).serializeArray();
        $(serializatedArray)
          .each(function(_k, v){
            return params[v.name] = v.value;
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
