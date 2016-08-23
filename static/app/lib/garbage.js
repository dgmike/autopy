'use strict';

angular.module('garbage', [])
  .factory('intentToRemoveFactory', [
    '$http', '$window', '$location',
    function intentToRemoveFactory($http, $window, $location) {
      return function (base_url) {
        return function intentToRemove(id) {
          swal({
              title:'Remover registro',
              text:'Tem certeza que deseja remover este registro? Esta ação não poderá ser desfeita.',
              showCancelButton: true,
              confirmButtonColor: "#DD6B55",
              confirmButtonText: "Sim, remova!",
              closeOnConfirm: false,
              showLoaderOnConfirm: true
            }, function() {
              $http
                .delete(base_url+id)
                .then(
                  function (response) {
                    swal(
                      {
                        title: 'Sucesso!',
                        text: 'O registro foi removido!',
                        type: 'success'
                      },
                      function () {
                        $location.path = base_url;
                        setTimeout(function () {
                          $window.location.reload();
                        }, 1000)
                      }
                    );
                  },
                  function (response) {
                    swal('Erro!', 'Houve um problema ao tentar remover o registro. Por favor, tente novamente mais tarde.', 'error');
                  }
                );
            }
          );
        };
      };
    }
  ]);
