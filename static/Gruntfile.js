module.exports = function(grunt) {

  grunt.initConfig({

    imagemin: {                          // Task
      dynamic: {                         // Another target
        options: {                       // Target options
          optimizationLevel: 3,
          svgoPlugins: [{ removeViewBox: false }]
        },
        files: [{
          expand: true,                  // Enable dynamic expansion
          cwd: 'static/img/',                   // Src matches are relative to this path
          src: ['*.{png,jpg,gif}'],   // Actual patterns to match
          dest: 'static/img_min/'                  // Destination path prefix
        }]
      }
    },

    watch: {
      files: ['<%= jshint.files %>'],
      tasks: ['jshint']
    },

    cssmin: {
      target: {
        files: [{
          expand: true,
          cwd: 'static/css/',
          src: ['*.css', '!*.min.css'],
          dest: 'static/css/',
          ext: '.min.css'
        }]
      }
    }
  });

  grunt.loadNpmTasks('grunt-contrib-imagemin');
  grunt.loadNpmTasks('grunt-contrib-watch');
  grunt.loadNpmTasks('grunt-contrib-cssmin');

  grunt.registerTask('default', ['imagemin', 'cssmin']);

};