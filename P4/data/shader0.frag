#define PROCESSING_COLOR_SHADER

#ifdef GL_ES
precision mediump float;
precision mediump int;
#endif

varying vec4 vertColor;
varying vec4 vertTexCoord;

void main() {
	float s = vertTexCoord.s * 3;
	s = (s - int(s)) * 2 - 1.0;

	float t = vertTexCoord.t * 3;
	t = (t - int(t)) * 2 - 1.0;

	float square = t*t + s*s;

	if (square < 0.5)
		gl_FragColor = vec4(0.2, 0.4, 1.0, 0.0);
	else
		gl_FragColor = vec4(0.2, 0.4, 1.0, 0.8);
}

