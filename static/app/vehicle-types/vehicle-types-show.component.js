'use strict';

angular
  .module('vehicleTypes')
  .component('vehicleTypesShow', {
    templateUrl: 'static/app/vehicle-types/vehicle-types-show.template.html',
    controller: [
      '$routeParams', '$http', '$location',
      function vehicleTypesShowController($routeParams, $http, $location) {
        self = this;

        $http({
          method: 'GET',
          url: '/api/vehicle-types/' + $routeParams.id,
        })
        .then(
          function successResponse(response) {
            self.vehicleType = response.data;
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

        self.intentToRemove = function intentToRemove(id) {
          swal(
            {
              title:'Remover tipo de veículo',
              text:'Tem certeza que deseja remover este tipo de veículo? Esta ação não poderá ser desfeita.',
              showCancelButton: true,
              confirmButtonColor: "#DD6B55",
              confirmButtonText: "Sim, remova!",
              closeOnConfirm: false,
              showLoaderOnConfirm: true
            },
            function(){
              setTimeout(function(){
                swal('Sucesso!', 'O registro de tipo de veículo foi removido!', 'success');
              }, 2000);
            }
          );
        }
      }
    ]
  });
