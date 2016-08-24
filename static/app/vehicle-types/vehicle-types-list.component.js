'use strict';

angular
  .module('vehicleTypes')
  .component('vehicleTypesList', {
    templateUrl: 'static/app/vehicle-types/vehicle-types-list.template.html',
    controller: [
      '$http', '$route', 'intentToRemoveFactory', '$location',
      function vehicleTypesListController($http, $route, intentToRemoveFactory, $location) {
        self = this;

        self.base_url = '#!/vehicle-types';
        self.search = $location.search().search;

        $http.get('/api/vehicle-types', {params: $route.current.params}).then(function (response) {
          self.per_page = response.data.per_page;
          self.currentPage = response.data.current_page;
          self.data = response.data;
        });

        self.changePerPage = function changePerPage(qty) {
          $route.updateParams({page:1, per_page: qty});
        }

        self.intentToRemove = intentToRemoveFactory('/api/vehicle-types/');
      }]
  });
