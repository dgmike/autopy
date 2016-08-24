'use strict';

angular
  .module('vehicleTypes')
  .component('vehicleTypesEdit', {
    templateUrl: 'static/app/vehicle-types/edit.template.html',
    controller: [
      '$routeParams', '$http', '$location', '$httpParamSerializer', '$scope',
      function vehicleTypesEditController($routeParams, $http, $location, $httpParamSerializer, $scope) {
        self = this;
        self.fields = ['name'];

        $http({
          'method': 'GET',
          'url': '/api/vehicle-types/' + $routeParams.id
        })
        .then(
          function successResponse(response) {
            $scope.resource = response.data;
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

        self.save = function save() {
          $('#edit-form')
            .find('.has-error').removeClass('has-error')
            .find('.help-block.error').remove();

          var params = {};
          $(self.fields).map(function (_k, item) {
            params[item] = $scope.resource[item];
          });
          $http({
            method: 'PUT',
            url: '/api/vehicle-types/' + $routeParams.id,
            data: params
            // headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
            // data: $httpParamSerializer(params)
          })
          .then(
            function success(response) {
              swal('Sucesso!', 'O registro foi salvo com sucesso.', 'success');
              var id = response.data.id;
              $location.path('/vehicle-types/' + id);
            },
            function error(response) {
              if (response.status != 403) {
                swal('Erro!', 'Ocorreu um problema ao salvar o registro. Por favor, tente novamente mais tarde.', 'error');
                return;
              }
              angular.forEach(response.data.errors, function (errors, key) {
                var field = $('[data-ng-model="resource.' + key + '"]');
                if (!field.length) {
                  console.warn('elemento nao encontrado: ' + errors);
                  return;
                }
                var formGroup = field.parents('.form-group');
                formGroup.addClass('has-error');
                $(errors).each(function (_k, errorMessage) {
                  var message = $('<span class="help-block error"></span>');
                  message.html(errorMessage);
                  formGroup.append(message);
                });
              });
              swal('Erro!', 'Houveram problemas ao salvar o registro. Por favor, analise o erros e tente novamente.');
            }
          );
        }
      }
    ]
  });
