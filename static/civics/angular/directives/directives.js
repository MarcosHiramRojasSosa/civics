angular.module('civics.directives', [])

/**
 *  Social widget block
 */
.directive('social', function(){
    return {
      restrict: 'A',
      templateUrl: 'static/civics/angular/directives/social_widget.html'
    }
})

/**
 *  Marker information in the maps
 */
.directive('markerInfo', function(){
    return {
        restrict: 'A',
        controller: 'MarkerinfoController',
        controllerAs: 'info',
        templateUrl: 'static/civics/angular/directives/marker-info.html',
        replace: true
    }
})

.controller('MarkerinfoController', function(Categories, $scope, meta){
     /** Root scope event fired from the services that create the markers **/
     $scope.$on('open-marker', angular.bind(this, function(event, args){
          this.expanded = true;
          this.marker = args;
          this.marker.topicname = Categories.topics[ this.marker.topics ];
          this.marker.agentname = Categories.agents[ this.marker.agents ];
          if(this.marker.spaces)
              this.marker.spacename = Categories.spaces[ this.marker.spaces ];
          if(this.marker.activities)
              this.marker.activitiesname = Categories.activities[ this.marker.activities ];
          this.showing = meta.showing;
          console.log(this.marker);
     }));
})

/**
 *  Marker information in the maps
 */
.directive('mapActions', function(){
    return {
        restrict: 'A',
        replace: true,
        templateUrl: 'static/civics/angular/directives/map-actions.html'
    }
})

/**
 *  Marker information in the maps
 */
.directive('leafletExpand', function(){
    return {
        restrict: 'A',
        replace: true,
        template: '<div class="leaflet-expand" ng-click="content.expand()"><span class="icon-expand"></span></div>',
    }
})

/**
 *  Marker information in the maps
 */
.directive('mapFilters', function(){
    return {
        restrict: 'A',
        replace: true,
        templateUrl: 'static/civics/angular/directives/map-filters.html'
    }
})

/**
 *  Marker information in the maps
 */
.directive('search', function(){
    return {
        restrict: 'A',
        replace: true,
        controller: 'SearchController',
        controllerAs: 'search',
        templateUrl: 'static/civics/angular/directives/search.html'
    }
})

.controller('SearchController', function($scope, $http, $rootScope, leafletData){
     this.results = [];

     this.query = function(){
        if(this.name.length > 3){
            $http.get('/api/autocomplete?n=' + this.name).then( angular.bind(this, function(response){
                if(response.data.length > 0)
                    this.results = response.data;
            }));
        } else {
            this.results = [];
        }
     };

     this.set = function(id){
        $http.get('/api/initiative?id=' + id).then( angular.bind(this, function(response){;
            $rootScope.$broadcast('open-marker', response.data);
            leafletData.getMap('civics-map').then(function(map){
                map.setView([response.data.lat, response.data.lng], 18)
            });
            this.results = [];
            this.name    = '';
        }));
     };
})

// /**
//  *  Marker information in the maps
//  */
// .directive('timesearch', function(){
//     return {
//         restrict: 'A',
//         replace: true,
//         controller: 'TimesearchController',
//         controllerAs: 'search',
//         templateUrl: 'static/civics/angular/directives/timesearch.html'
//     }
// })
//
// .controller('TimesearchController', function($scope, $http, $rootScope, leafletData){
//
// });
