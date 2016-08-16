'use strict';

angular
  .module('vehicleTypes')
  .component('vehicleTypesEdit', {
    templateUrl: 'static/app/vehicle-types/vehicle-types-edit.template.html',
    controller: [
      '$routeParams',
      function vehicleTypesEditController($routeParams) {
        this.vehicleType = {
          id: $routeParams.id,
          name: 'Carro'
        };
      }
    ]
  });
