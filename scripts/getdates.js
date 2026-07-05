// Populate current year and document last modified
document.addEventListener('DOMContentLoaded', function(){
  const yearEl = document.getElementById('currentyear');
  if(yearEl){
    yearEl.textContent = new Date().getFullYear();
  }

  const lm = document.getElementById('lastModified');
  if(lm){
    lm.textContent = 'Last modified: ' + document.lastModified;
  }
});
