'use strict';

angular
  .module('vehicles')
  .component('vehiclesShow', {
    templateUrl: 'static/app/vehicles/show.template.html',
    controller: [
      '$scope', '$routeParams', '$http', '$location', 'intentToRemoveFactory',
      function vehiclesShowController($scope, $routeParams, $http, $location, intentToRemoveFactory) {
        self = this;

        $http({
          method: 'GET',
          url: '/api/vehicles/' + $routeParams.id,
        })
        .then(
          function successResponse(response) {
            $scope.vehicle = response.data;
          },
          function errorResponse(response) {
            if (response.status != 404) {
              swal('Erro!', 'Ocorreu um problema na sua requisição. Por favor, tente novamente mais tarde.', 'error');
              return;
            }
            swal('Não encontrado', 'Desculpe, mas o registro procurado não foi encontrado.', 'error');
            $location.path('/vehicles');
          }
        );

        self.intentToRemove = intentToRemoveFactory('/api/vehicles/');
      }
    ]
  });
