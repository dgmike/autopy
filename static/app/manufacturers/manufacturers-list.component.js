'use strict';

angular
  .module('manufacturers')
  .component('manufacturersList', {
    templateUrl: 'static/app/manufacturers/manufacturers-list.template.html',
    controller: [
      '$http', '$route', 'intentToRemoveFactory', '$location',
      function manufacturersListController($http, $route, intentToRemoveFactory, $location) {
        self = this;

        self.base_url = '#!/manufacturers';
        self.search = $location.search().search;


        $http.get('/api/manufacturers', {params: $route.current.params}).then(function (response) {
          self.per_page = response.data.per_page;
          self.currentPage = response.data.current_page;
          self.data = response.data;
        });

        self.changePerPage = function changePerPage(qty) {
          $route.updateParams({page:1, per_page: qty});
        }

        self.intentToRemove = intentToRemoveFactory('/api/manufacturers/');
      }]
  });
