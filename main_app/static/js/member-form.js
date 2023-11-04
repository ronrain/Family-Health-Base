const birthDateInput = document.getElementById('id_birth_date');
const updateDateInput = document.getElementById('id_update_date');

const picker = MCDatepicker.create({
  dateFormat: 'yyyy-mm-dd',
  closeOnBlur: true,
  selectedDate: new Date(),
});

birthDateInput.addEventListener("click", (evt) => {
  picker.open();
});

updateDateInput.addEventListener("click", (evt) => {
  picker.open();
});
