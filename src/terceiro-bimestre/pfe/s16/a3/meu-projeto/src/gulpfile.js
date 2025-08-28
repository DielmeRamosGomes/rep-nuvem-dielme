const gulp = require('gulp');
const sass = require('gulp-sass')(require('sass'));
const cleanCSS = require('gulp-clean-css');
// Tarefa para compilar SASS para CSS
gulp.task('sass', function() {
return gulp.src('src/scss/*.scss') // Arquivos de entrada SASS
.pipe(sass()) // Compila SASS para CSS
.pipe(cleanCSS()) // Minifica o CSS
.pipe(gulp.dest('dist/css')); // Pasta de saída
});
// Tarefa para observar mudanças
gulp.task('watch', function() {
gulp.watch('src/scss/*.scss', gulp.series('sass'));
});