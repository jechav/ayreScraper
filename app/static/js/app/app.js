angular.module('app', [])
.run(['$rootScope', 
     function ($rootScope) {
  console.info('llegamos');
}])
.controller('main', ['$scope', 'Ayre', '$timeout',
            function($scope, Ayre, $timeout){

  $scope.user = {};

  $scope.busy = false;
  $scope.results = null;

  $scope.makeRequest = function(){
    console.log($scope.user);
    $scope.busy = true;
    $scope.results = null;

    Ayre.auth($scope.user, success, error);

    function success(res){
      $scope.results = res.data;
      $scope.busy = false;
      console.log($scope.results);
    }
    function error(res){
      console.warn(res);
      alert( JSON.stringify(res.data.error) );
      $scope.busy = false;
    }

  };

}])
.service('Ayre', ['$http',
         function($http){

  this.URL = '/';
  this.auth = function(data, callback, error){
    var conf = {
      url: this.URL,
      method: 'POST',
      data: $.param(data),
      headers: { 'Content-Type': 'application/x-www-form-urlencoded' }
    }
    //console.warn( conf );
    return $http(conf).then(callback, error);
    //return $http.post(this.URL, data).then(callback, error);
  }

}])

.directive('t3bsLoading', [function(){
  return {
    restrict: 'A',
    scope: {
      t3bsLoading: '='
    },
    link: function(scope, element, attrs) {
      element.css('position', 'relative');

      var tmp = '<load style="position: absolute; top: 0; bottom: 0; left: 0; \
      right: 0; background-color: rgba(255, 255, 255, 0.75);"> <img \
      src="https://mir-s3-cdn-cf.behance.net/project_modules/disp/585d0331234507.564a1d239ac5e.gif" \
      alt="Loading" style="height: 120px; position: absolute; top: 150px; \
      left: 50%; transform: translate(-50%, 0);"> \
      </load>'

      scope.$watch('t3bsLoading', function(){
        if(scope.t3bsLoading){
          element.append(tmp)
        }else{
          element.find('load').remove();
        }
      });
    }
  };
}])
