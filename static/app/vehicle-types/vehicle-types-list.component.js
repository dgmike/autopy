'use strict';

angular
  .module('vehicleTypes')
  .component('vehicleTypesList', {
    templateUrl: 'static/app/vehicle-types/vehicle-types-list.template.html',
    controller: function vehicleTypesListController($http) {
      self = this;

      self.currentPage = null;

      self.goToPage = function (page) {
        var perPage = 20;
        if (!page || page == self.currentPage) {
          return;
        }
        $http.get('/api/vehicle-types?per_page=' + perPage + '&page=' + page).then(function (response) {
          self.currentPage = response.data.current_page;
          self.data = response.data;
        });
      };

      self.goToPage(1);

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
