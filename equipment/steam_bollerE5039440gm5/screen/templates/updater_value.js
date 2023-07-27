function updateValues() {
  $.ajax({
    url: '/K5LCV1',
    dataType: 'json', // Предполагаем, что данные ответа в формате JSON
    success: function(data) {
    $('#K5LCV1').text(data.K5LCV1);
    }
  });

  $.ajax({
    url: '/K5LCV1_1',
    dataType: 'json', // Предполагаем, что данные ответа в формате JSON
    success: function(data) {
    $('#K5LCV1_1').text(data.K5LCV1_1);
    }
  });

  $.ajax({
    url: '/K5F5',
    dataType: 'json', // Предполагаем, что данные ответа в формате JSON
    success: function(data) {
    $('#K5F5').text(data.K5F5);
    }
  });

  $.ajax({
    url: '/K5T16',
    dataType: 'json', // Предполагаем, что данные ответа в формате JSON
    success: function(data) {
    $('#K5T16').text(data.K5T16);
    }
  });

  setTimeout(updateValues, 1000);
}

$(document).ready(function() {
  updateValues();
});