#define PROCESSING_COLOR_SHADER

#ifdef GL_ES
precision mediump float;
precision mediump int;
#endif

varying vec4 vertColor;
varying vec4 vertTexCoord;

void main() {
	float x0 = vertTexCoord.s * 3.5 - 2.5;
	float y0 = vertTexCoord.t * 3.0 - 1.5;
	float x = 0.0;
	float y = 0.0;
	int iteration = 0;
	int max_iteration = 20;
	while (x*x + y*y < 2*2 && iteration < max_iteration) {
		float xtemp = x*x - y*y + x0;
		y = 2*x*y + y0;
		x = xtemp;
		iteration = iteration + 1;
	}
	if (iteration == max_iteration)
		gl_FragColor = vec4(1.0, 1.0, 1.0, 1.0);
	else
		gl_FragColor = vec4(1.0, 0.0, 0.0, 1.0);
}

