'use strict';

angular
  .module('vehicleTypes')
  .component('vehicleTypesList', {
    templateUrl: 'static/app/vehicle-types/vehicle-types-list.template.html',
    controller: function vehicleTypesList() {
      self = this;

      self.vehicleTypes = [
        { id: 1, name: 'Carro' },
        { id: 2, name: 'Moto' }
      ];

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
    },
  });
