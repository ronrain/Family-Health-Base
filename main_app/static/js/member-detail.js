const dateInput = document.getElementById('id_date');

  const picker = MCDatepicker.create({
    dateFormat: 'yyyy-mm-dd',
    closeOnBlur: true,
    selectedDate: new Date(),
  });

  dateInput.addEventListener("click", (evt) => {
    picker.open();
  });