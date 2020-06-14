import {DatePicker, 
	Button, FormModel, 
	Form, Upload, Layout, 
	Select, Input, InputNumber,
	 Radio, Switch, Checkbox,
	 Slider, Icon, Tag, Table} from 'ant-design-vue';
import axios from 'axios';
import Vue from 'vue';
import Router from 'vue-router';
import HelloWorld from '@/components/HelloWorld';
import StudentRegister from '@/components/StudentRegister';
import Applications from '@/components/Applications';

Vue.use(DatePicker);
Vue.use(Button);
Vue.use(Router);
Vue.use(Form)
Vue.use(FormModel);
Vue.use(Layout);
Vue.use(Select);
Vue.use(Input);
Vue.use(Upload);
Vue.use(Radio);
Vue.use(InputNumber);
Vue.use(Switch);
Vue.use(Checkbox);
Vue.use(Slider);
Vue.use(axios);
Vue.use(Icon);
Vue.use(Tag);
Vue.use(Table);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld,
    },
    {
    	path: '/student/register',
    	name: 'StudentRegister',
    	component: StudentRegister,
    },
    {
    	path: '/applications',
    	name: 'Applications',
    	component: Applications
    }
  ],
});
