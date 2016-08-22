'use strict';

angular
  .module('vehicleTypes')
  .component('vehicleTypesList', {
    templateUrl: 'static/app/vehicle-types/vehicle-types-list.template.html',
    controller: function vehicleTypesListController($http, $route) {
      self = this;

      $http.get('/api/vehicle-types', {params: $route.current.params}).then(function (response) {
        self.per_page = response.data.per_page;
        self.currentPage = response.data.current_page;
        self.data = response.data;
      });

      self.changePerPage = function changePerPage(qty) {
        $route.updateParams({page:1, per_page: qty});
      }

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
