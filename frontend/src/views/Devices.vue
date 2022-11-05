<template>
  <section>
    <p>Devices</p>

    <table class="table table-striped">
  <thead>
    <tr>
      <th>Name</th>
      <th>Value</th>
      <th>Status</th>
    </tr>
  </thead>
  <tbody>
    <tr v-for="device in devices" :key="device">
       <th>{{ device.name }}</th> 
       <td>{{ device.value }}</td>  
       <td>{{ device.status }}</td>  
    </tr>
   </tbody>
</table>
    <div id="app">
      <router-view></router-view>
    </div>
  </section>

</template>

<!-- <script>
export default {
  data() {
    return {
      devices: [
  {
    "fixed": "",
    "visibility": [
      "namespace",
      "metadata",
      "devlist"
    ],
    "name": "coll",
    "unit": "",
    "precision": 0,
    "warnlimits": null,
    "fixedby": null,
    "requires": {},
    "pollinterval": 5,
    "maxage": 12,
    "loglevel": "info",
    "target": "15m",
    "fallback": null,
    "mapping": {
      "off": 0,
      "10m": 2,
      "15m": 4,
      "20m": 8
    },
    "fmtstr": "%.3f",
    "blockingmove": true,
    "description": "collimation",
    "classes": [
      "nicos.devices.generic.switcher.Switcher",
      "nicos.devices.abstract.MappedMoveable",
      "nicos.devices.abstract.MappedReadable",
      "nicos.core.mixins.HasMapping",
      "nicos.core.mixins.DeviceMixinBase",
      "nicos.devices.abstract.TransformedMoveable",
      "nicos.devices.abstract.TransformedReadable",
      "nicos.core.device.Moveable",
      "nicos.core.device.Waitable",
      "nicos.core.device.Readable",
      "nicos.core.device.Device",
      "builtins.object"
    ],
    "value": "15m",
    "status": [
      200,
      ""
    ]
  },
  {
    "classes": [
      "nicos.devices.instrument.Instrument",
      "nicos.core.device.Device",
      "builtins.object"
    ],
    "responsible": "R. Esponsible <r.esponsible@frm2.tum.de>",
    "description": "demo instrument",
    "facility": "NICOS demo instruments",
    "instrument": "DEMO",
    "countloopdelay": 0.025,
    "doi": "",
    "operators": [
      "NICOS developer team"
    ],
    "website": "http://www.nicos-controls.org",
    "loglevel": "info",
    "visibility": [
      "namespace",
      "metadata",
      "devlist"
    ],
    "name": "demo"
  },
  {
    "classes": [
      "nicos.devices.generic.detector.GatedDetector",
      "nicos.devices.generic.detector.Detector",
      "nicos.core.device.Measurable",
      "nicos.core.device.Waitable",
      "nicos.core.device.Readable",
      "nicos.core.device.Device",
      "builtins.object"
    ],
    "visibility": [
      "namespace",
      "metadata",
      "devlist"
    ],
    "response_topic": "TEST_histResponse",
    "fmtstr": "det1_timer = %.3f, det1_mon1 = %d, det1_mon2 = %d, roi1 = %d, det1_img.sum = %d",
    "brokers": [
      "ess01.psi.ch:9092"
    ],
    "command_topic": "TEST_histCommands",
    "description": "demo 2D detector",
    "loglevel": "info",
    "disablevalues": [],
    "maxage": 12,
    "ack_timeout": 5,
    "enablevalues": [],
    "pollinterval": 5,
    "name": "det",
    "unit": "",
    "postprocess": [
      [
        "roi1",
        "det1_img"
      ]
    ],
    "status_topic": "TEST_histHeartbeat",
    "saveintervals": [],
    "warnlimits": null,
    "liveinterval": 1,
    "status": [
      200,
      "roi1=idle, det1_img=idle, det1_mon1=idle, det1_mon2=idle, det1_timer=idle"
    ]
  },],
    devs: []
    }
  }
}
</script> /-->

<script>
export default {
  data() {
    console.println('hello')
    return { devices: [] }
  },
  created() {
    this.fetchName();
  },
  watch: {
    // Re-fetch when route changes
    '$route': 'fetchName'
  },
  methods: {
    fetchName() {
      this.devices =  this.$route.devices
    }
  }
}
</script>
