<script type="text/javascript">
    $('.datepicker').datepicker({
        dateFormat: 'yy-mm-dd',
    startDate: '-3d'
    });
</script>
<form id="loanForm">
  <div class="form-group">
    <label for="amount">Cantidad</label>
    <input type="number" class="form-control" id="amount" name="amount">
  </div>
  <div class="form-group">
    <label for="due_date">Fecha de vencimiento</label>
      <br>
      <input class="datepicker" id="due_date" name="due_date" data-date-format="yyyy-mm-dd">
  </div>
</form>