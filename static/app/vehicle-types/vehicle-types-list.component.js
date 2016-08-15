'use strict';

angular
  .module('vehicleTypes')
  .component('vehicleTypesList', {
    templateUrl: 'static/app/vehicle-types/vehicle-types-list.template.html',
    controller: function vehicleTypesList() {
      this.vehicleTypes = [
        { id: 1, name: 'Carro' },
        { id: 2, name: 'Moto' }
      ]
    }
  });
