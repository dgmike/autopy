'use strict';

angular
  .module('manufacturers')
  .component('manufacturersShow', {
    templateUrl: 'static/app/manufacturers/show.template.html',
    controller: [
      '$scope', '$routeParams', '$http', '$location', 'intentToRemoveFactory',
      function ManufacturersShowController($scope, $routeParams, $http, $location, intentToRemoveFactory) {
        self = this;

        $http({
          method: 'GET',
          url: '/api/manufacturers/' + $routeParams.id,
        })
        .then(
          function successResponse(response) {
            $scope.manufacturer = response.data;
          },
          function errorResponse(response) {
            if (response.status != 404) {
              swal('Erro!', 'Ocorreu um problema na sua requisição. Por favor, tente novamente mais tarde.', 'error');
              return;
            }
            swal('Não encontrado', 'Desculpe, mas o registro procurado não foi encontrado.', 'error');
            $location.path('/manufacturers');
          }
        );

        self.intentToRemove = intentToRemoveFactory('/api/manufacturers/');
      }
    ]
  });
