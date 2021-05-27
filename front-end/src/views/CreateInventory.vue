<template>
  <div class="container">
    <section class="section">
      <form @submit.prevent>
        <div class="columns">
          <div class="column is-half is-offset-one-quarter">
            <h1 class="title">
              Create Inventory
              <span class="icon has-text-info ml-2">
                <i class="fa fa-cubes" aria-hidden="true"></i>
              </span>
            </h1>
            <div class="field">
              <label class="label" for="Name">Name: </label>
              <div class="control">
                <input class="input" type="text" placeholder="Item name...">
              </div>
            </div>
            <div class="field">
              <label class="label" for="Name">Price: </label>
              <div class="control">
                <input class="input" type="number" placeholder="Item Price...">
              </div>
            </div>
            <div class="field">
              <label class="label" for="Name">Stock Qty: </label>
              <div class="control">
                <input class="input" type="number" placeholder="Item Stock Qty...">
              </div>
            </div>
            <div class="file is-boxed">
              <label class="file-label">
                <input class="file-input" type="file" name="resume">
                <span class="file-cta">
                  <span class="file-icon">
                    <i class="fa fa-upload"></i>
                  </span>
                  <span class="file-label">
                    Choose a file…
                  </span>
                </span>
              </label>
            </div>
            <div class="columns mt-2">
              <div class="column">
                <div class="control">
                  <button class="button is-link mr-3">Submit</button>
                  <button class="button is-danger">Cancel</button>
                </div>
              </div>
            </div>
          </div>
        </div> <!-- end columns -->
      </form>
    </section>
  </div>
</template>
