#define PROCESSING_TEXTURE_SHADER

#ifdef GL_ES
precision mediump float;
precision mediump int;
#endif

uniform sampler2D texture;

varying vec4 vertColor;
varying vec4 vertTexCoord;

void main() {
	float thisx = vertTexCoord.x;
	float thisy = vertTexCoord.y;
	float c = 0.005;

	vec4 p = texture2D(texture, vec2(thisx, thisy));

	vec4 p1 = texture2D(texture, vec2(thisx-c, thisy));
	vec4 p2 = texture2D(texture, vec2(thisx+c, thisy));
	vec4 p3 = texture2D(texture, vec2(thisx, thisy-c));
	vec4 p4 = texture2D(texture, vec2(thisx, thisy+c));

	float r = p1.r + p2.r + p3.r + p4.r - 4 * p.r;
	float g = p1.g + p2.g + p3.g + p4.g - 4 * p.g;
	float b = p1.b + p2.b + p3.b + p4.b - 4 * p.b;
	float gray = 5 * (r * 0.3 + g * 0.6 + b * 0.1);
	gl_FragColor = vec4(gray, gray, gray, 1.0);
}

