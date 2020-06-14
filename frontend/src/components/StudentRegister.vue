<template>
  <a-form
    id="components-form-demo-validate-other"
    :form="form"
    v-bind="formItemLayout"
    @submit="handleSubmit"
  >
    <a-form-item label="Fullname" has-feedback>
      <a-input
        v-decorator="[
          'fullnames',
          { rules: [{ required: true, message: 'Please provide your legal names' }] },
        ]"
        placeholder="Legal Name"
      >
      </a-input>
    </a-form-item>
    <a-form-item label="Email" has-feedback>
      <a-input
        v-decorator="[
          'email',
          { rules: [{ required: true, message: 'Please provide your email address.' }] },
        ]"
        placeholder="Email address"
      >
      </a-input>
    </a-form-item>
    <a-form-item label="Username" has-feedback>
      <a-input
        v-decorator="[
          'username',
          { rules: [{ required: true, message: 'Please provide your provide a username' }] },
        ]"
        placeholder="Username"
      >
      </a-input>
    </a-form-item>
    <a-form-item label="School" has-feedback>
      <a-select
        v-decorator="[
          'school',
          { rules: [{ required: true, message: 'Please select your institution' }] },
        ]"
        placeholder="Please select your institution"
      >
        <a-select-option value="china">
          China
        </a-select-option>
        <a-select-option value="usa">
          U.S.A
        </a-select-option>
      </a-select>
    </a-form-item>

    <a-form-item label="Course" has-feedback>
      <a-select
        v-decorator="[
          'course',
          {
            rules: [
              { required: true, message: 'Please select your course' },
            ],
          },
        ]"
        placeholder="Your course"
      >
        <a-select-option value="red">
          Red
        </a-select-option>
        <a-select-option value="green">
          Green
        </a-select-option>
        <a-select-option value="blue">
          Blue
        </a-select-option>
      </a-select>
    </a-form-item>
    <a-form-item label="National ID" required has-feedback>
      <div class="dropbox">
        <a-upload-dragger
          v-decorator="[
            'national_id',
            {
              valuePropName: 'birth',
              getValueFromEvent: handleNational,
              customRequest: customRequest,

            },
          ]"
          name="national_id"
        >
          <p class="ant-upload-drag-icon">
            <a-icon type="inbox" />
          </p>
          <p class="ant-upload-text">
            Click or drag National ID file to this area to upload
          </p>
          <p class="ant-upload-hint">
            Support for a single or bulk upload.
          </p>
        </a-upload-dragger>
      </div>
    </a-form-item>
     <a-form-item label="Birth Certificate" required has-feedback>
      <div class="dropbox">
        <a-upload-dragger
          v-decorator="[
            'birth_certificate',
            {
              valuePropName: 'birth',
              getValueFromEvent: handleBirth,
              customRequest: customRequest,
            },
          ]"
          name="birth_certificate"
        >
          <p class="ant-upload-drag-icon">
            <a-icon type="inbox" />
          </p>
          <p class="ant-upload-text">
            Click or drag Birth Certificate file to this area to upload
          </p>
          <p class="ant-upload-hint">
            Supports for PDF files only.
          </p>
        </a-upload-dragger>
      </div>
    </a-form-item>

    <a-form-item :wrapper-col="{ span: 12, offset: 6 }">
      <a-button type="primary" html-type="submit">
        Submit
      </a-button>
    </a-form-item>
  </a-form>
</template>

<script>
	import axios from 'axios';
export default {
  data: () => ({
    formItemLayout: {
      labelCol: { span: 6 },
      wrapperCol: { span: 14 },
    },
  }),
  beforeCreate() {
    this.form = this.$form.createForm(this, { name: 'validate_other' });
  },
  methods: {
    handleSubmit(e) {
      e.preventDefault();
      this.form.validateFields((err, values) => {
        if (!err) {
            console.log(JSON.stringify(values));
            console.log(values);
        }
      });
    },
    handleNational(e) {
    	console.log(this.$refs);
      console.log('Upload event national:', e);
      if (Array.isArray(e)) {
        return e;
      }
      return e && e.fileList;
    },

    handleBirth(e){
    	console.log(this.$refs);
	    console.log('Upload event birth:', e);
	      if (Array.isArray(e)) {
	        return e;
	      }
	      return e && e.fileList;
    },
    customRequest(e){
    	console.log(e+" It is jere");
    }
  },
};
</script>
<style>
#components-form-demo-validate-other .dropbox {
  height: 180px;
  line-height: 1.5;
}
</style>