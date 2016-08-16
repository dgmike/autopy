'use strict';

angular
  .module('vehicleTypes')
  .component('vehicleTypesShow', {
    templateUrl: 'static/app/vehicle-types/vehicle-types-show.template.html',
    controller: [
      '$routeParams',
      function vehicleTypesShowController($routeParams) {
        self = this;

        self.vehicleType = {
          id: $routeParams.id,
          name: 'Carro'
        };

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
