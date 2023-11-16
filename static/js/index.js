const cakeSizeField = document.getElementById('id_cake_size');
  const cakeOtherSizeLabel = document.querySelector('label[for="id_cake_other_size"]');
  const cakeOtherSizeField = document.getElementById('id_cake_other_size');

  cakeOtherSizeField.style.display = 'none';
  cakeOtherSizeLabel.style.display = 'none';

  cakeSizeField.addEventListener('change', function() {
      if (cakeSizeField.value === 'other') {
          cakeOtherSizeLabel.style.display = 'inline-block';
          cakeOtherSizeField.style.display = 'block';
          cakeOtherSizeField.querySelector('input').required = true;
          
      } else {
          cakeOtherSizeLabel.style.display = 'none';
          cakeOtherSizeField.style.display = 'none';
          cakeOtherSizeField.querySelector('input').required = false;
          
      }
  });