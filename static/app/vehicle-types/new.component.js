'use strict';

angular
  .module('vehicleTypes')
  .component('vehicleTypesNew', {
    templateUrl: 'static/app/vehicle-types/new.template.html',
    controller: function VehicleTypesNewController($scope, $location, $route, $http, $httpParamSerializer) {
      var self = this;

      self.fields = ['name'];

      self.intentToSave = function () {
        $scope;
        var params = {};
        $(self.fields).map(function (_k, item) {
          params[item] = $scope[item];
        });
        $('#create-form')
          .find('.has-error').removeClass('has-error')
          .find('.help-block.error').remove();

        $http({
          method: 'POST',
          url: '/api/vehicle-types',
          headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
          data: $httpParamSerializer(params)
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
              var field = $('[data-ng-model=' + key + ']');
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
      };
    }
  });
