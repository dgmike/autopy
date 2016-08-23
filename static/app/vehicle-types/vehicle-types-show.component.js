'use strict';

angular
  .module('vehicleTypes')
  .component('vehicleTypesShow', {
    templateUrl: 'static/app/vehicle-types/vehicle-types-show.template.html',
    controller: [
      '$scope', '$routeParams', '$http', '$location', 'intentToRemoveFactory',
      function vehicleTypesShowController($scope, $routeParams, $http, $location, intentToRemoveFactory) {
        self = this;

        $http({
          method: 'GET',
          url: '/api/vehicle-types/' + $routeParams.id,
        })
        .then(
          function successResponse(response) {
            $scope.vehicleType = response.data;
          },
          function errorResponse(response) {
            if (response.status != 404) {
              swal('Erro!', 'Ocorreu um problema na sua requisição. Por favor, tente novamente mais tarde.', 'error');
              return;
            }
            swal('Não encontrado', 'Desculpe, mas o registro procurado não foi encontrado.', 'error');
            $location.path('/vehicle-types');
          }
        );

        self.intentToRemove = intentToRemoveFactory('/api/vehicle-types/');
      }
    ]
  });
